/*
  * This program text file is part of the CS-A1120 Programming 2 course
  * materials at Aalto University in Spring 2021. The programming exercises
  * at CS-A1120 are individual and confidential assignments---this means
  * that as a student taking the course you are allowed to individually
  * and confidentially work with the material, to discuss and review the
  * material with course staff, as well as to submit the material for grading
  * on course infrastructure. All other use, including in particular
  * distribution of the material or exercise solutions, is forbidden and
  * constitutes a violation of the code of conduct at this course.
  *
  */

package examGrader
import scala.collection.immutable._
import scala.annotation.varargs

/**
 * An immutable class that provides handy methods for obtaining statistics of
 * an exam of a course.
 * Please see the UnitTests class for usage examples.
 * @param studentDB is the student database, associating non-course related information
 *   (name, study programme etc) to each student id
 * @param homeworkDone is the set of students who have done their homework and thus
 *   the set of students whose exam will be graded.
 *   The students who have not completed the homework do not get ANY grade, not even 0.
 * @param bonusPoints associates bonus points to some of the students
 * @param examPoints maps each student id that has taken the exam to a list of exam assignment points.
 * @param gradeLimits is the list of lower points for grades 1, 2, 3, 4, and 5.
 *   For example, if gradeLimits = List(30,36,42,48,54) and a student gets 36 points, then s/he
 *   will get the grade 2 (provided that the homework is done, of course).
 *   On the other hand, if a student gets 27 points, then his/her grade will be 0 (failed).
 *
 * NOTE: this is an exercise on functional programming style.
 * Therefore, you are NOT allowed to use mutable data structures or vars.
 */
class ExamGrader(val studentDB: StudentDB,
  val homeworkDone: Seq[StudentId],
  val bonusPoints: Map[StudentId, Int],
  val examPoints: Map[StudentId, List[Int]],
  val gradeLimits: List[Int]) {

  // Check that the student ids in other lists are also in studentDB
  homeworkDone.foreach(id => require(studentDB.students.contains(id), "Unknown student " + id + " in homework list"))
  bonusPoints.keys.foreach(id => require(studentDB.students.contains(id), "Unknown student " + id + " in bonus points list"))
  examPoints.keys.foreach(id => require(studentDB.students.contains(id), "Unknown student " + id + " in exam points list"))
  // Check that the gradeLimits list is of correct length and that the grade limits are increasing.
  require(gradeLimits.length == 5 && (gradeLimits zip gradeLimits.tail).forall(p => p._1 < p._2))

  /**
   * The list of students whose exam is graded, i.e. those that
   * appear in both examPoints and homeworkDone.
   * Hints: the methods "keys" of Map as well as "filter" and "toSet" of Seq/List/etc may be useful.
   * Note: "lazy" means that this is computed when needed for the first time, not necessarily
   * immediately when an object of this class is created.
   */
  lazy val graded: Set[StudentId] = homeworkDone.filter(x => examPoints.contains(x)).toSet

  /**
   * Return the grade (0, 1, 2, 3, 4, or 5) that is obtained with n points.
   * See the explanation in the comments/documentation of the class above.
   */
  def pointsToGrade(n: Int): Int = {
    if (n >= gradeLimits(4)) {
      5
    } else if (n >= gradeLimits(3)) {
      4
    } else if (n >= gradeLimits(2)) {
      3
    } else if (n >= gradeLimits(1)) {
      2
    } else if (n >= gradeLimits(0)) {
      1
    } else {
      0
    }

  }
  
  /**
   * The sum of bonus and exam assignment points of a student.
   * May only be called for students who have exam points.
   * But note that a student may not appear on the list of bonus points receivers, meaning
   * that s/he will have 0 bonus points.
   */
  def points(id: StudentId): Int = {
    require(examPoints.contains(id))

    val outexam = examPoints.filter(x => x._1 == id).values.flatten.sum
    val outbonus = bonusPoints.filter(x => x._1 == id).values.sum
    outexam + outbonus
  }

  /**
   * The grades of the students whose exam is graded.
   * The grade of a student is determined by computing the sum of his/her bonus and exam points,
   * and then taking the grade from the gradeLimits.
   */
  lazy val grades: Map[StudentId, Int] = {
    val out1 = (graded zip graded).toMap.values.map(x => pointsToGrade(points(x)))
    val out2 = (graded zip out1).toMap
    out2
  
  }
  
  /**
   * Return the n best students, best first, with respect to the points obtained
   * (again, only the students whose exam is graded are taken into account).
   * Breaking ties can be arbitrary: for instance, if 5 students got full points and 3 best
   * students are requested, you can return any 3 of those 5.
   */
  def bestStudents(n: Int): Seq[StudentId] = {
    val out = grades.keys.map(x => (x, points(x))).toVector
    val out2 = out.sortBy(x => x._2)
    val out3 = out2.reverse.take(n).map(x => x._1)
    out3.toSeq
  }

  /**
   * Return a map associating each grade {0,...,5} to the set of students who obtained that grade.
   * If no students obtained some grade (e.g. 3), then an empty set should be associated to it.
   */
  def studentsByGrade: Map[Int, Set[StudentId]] = {
    val range = 0 to 5
    val out = grades.groupBy(x => x._2)
    val out2 = out.map(x => (x._1, x._2.map(x => x._1).toSet))
    val out3 = range.map(x => (x, out2.getOrElse(x, Set())))
    out3.toMap
  }
  
  /**
   * The set of study programmes whose students took the exam and whose exam was graded.
   */
  def gradedProgrammes: Set[StudyProgramme] = graded.map(x => studentDB.programmeOf(x))

  /**
   * Associate each study programme whose students were graded in the exam to
   * a sub-map of "grades" restricted to the students of that programme.
   * For those study programs whose students were not graded the resulting map
   * should be undefined.
   */
  def gradesByProgramme: Map[StudyProgramme, Map[StudentId, Int]] = grades.groupBy(x => studentDB.programmeOf(x._1))

}

